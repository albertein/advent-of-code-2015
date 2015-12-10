import re
import sys


class Node(object):

    def __init__(self):
        self.destination_nodes = []
        self._output_signal = None


    def reset(self):
        pass


    def connect(self, node):
        self.destination_nodes.append(node)


    def _process_output(self):
        for node in self.destination_nodes:
            node.input_ready(self)


    @property
    def output_signal(self):
        return self._output_signal & 0xFFFF # Mask to 16 bits
    

    @output_signal.setter
    def output_signal(self, value):
        self._output_signal = value



class SingleInputNode(Node):

    def __init__(self):
        self.signal = None
        super(SingleInputNode, self).__init__()


    def reset(self):
        self.signal = None
        self.output_signal = None


    def input_ready(self, node):
        self.signal = node.output_signal
        self.output_signal = self.signal
        self._process_output()


class Wire(SingleInputNode):
    pass


class Signal(SingleInputNode):

    def __init__(self, signal):
        super(Signal, self).__init__()
        self.output_signal = signal


    def pulse(self):
        self._process_output()


class RShiftNode(SingleInputNode):

    def __init__(self, shift_by):
        super(RShiftNode, self).__init__()
        self.shift_by = shift_by


    def _process_output(self):
        self.output_signal = self.signal >> self.shift_by
        super(RShiftNode, self)._process_output()


class LShiftNode(SingleInputNode):

    def __init__(self, shift_by):
        self.shift_by = shift_by
        super(LShiftNode, self).__init__()


    def _process_output(self):
        self.output_signal = self.signal << self.shift_by
        super(LShiftNode, self)._process_output()


class NOTNode(SingleInputNode):

    def _process_output(self):
        self.output_signal = ~self.signal
        super(NOTNode, self)._process_output()


class DoubleInputNode(Node):

    def __init__(self, left_node, right_node):
        self.left_signal = None
        self.right_signal = None
        self.left_node = left_node
        self.right_node = right_node
        self.left_node.connect(self)
        self.right_node.connect(self)
        super(DoubleInputNode, self).__init__()


    def reset(self):
        self.left_signal = None
        self.right_signal = None
        self.output_signal = None


    def input_ready(self, node):
        if node == self.left_node:
            self.left_signal = node.output_signal
        else:
            self.right_signal = node.output_signal

        if self.left_signal != None and self.right_signal != None:
            self._process_output()


class ANDNode(DoubleInputNode):

    def _process_output(self):
        self.output_signal = self.left_signal & self.right_signal
        super(ANDNode, self)._process_output()


class ORNode(DoubleInputNode):
    def _process_output(self):
        self.output_signal = self.left_signal | self.right_signal
        super(ORNode, self)._process_output()



if __name__ == "__main__":

    BINARY_GATES = {
        'AND': ANDNode,
        'OR': ORNode
    }

    SHIFT_GATES = {
        'RSHIFT': RShiftNode,
        'LSHIFT': LShiftNode
    }

    signals = {}
    wires = {}

    def get_wire(name):

        if re.match('^\d+$', name): # Signal, not wire
            value = int(name)
            signal = signals.get(value)
            if not signal:
                signal = Signal(value)
                signals[value] = signal
            return signal


        wire = wires.get(name)
        if not wire:
            wire = Wire()
            wires[name] = wire
        return wire


    input_file = open(sys.argv[1], 'r')
    instructions = input_file.readlines()

    for instruction in instructions:
        section = instruction.strip().split()
        
        if section[1] in BINARY_GATES.keys():
            left_wire = get_wire(section[0])
            right_wire = get_wire(section[2])
            output_wire = get_wire(section[4])
            node = BINARY_GATES.get(section[1])(left_wire, right_wire)
            node.connect(output_wire)
        elif section[1] in SHIFT_GATES.keys():
            input_wire = get_wire(section[0])
            output_wire = get_wire(section[4])
            shift_value = int(section[2])
            node = SHIFT_GATES.get(section[1])(shift_value)
            input_wire.connect(node)
            node.connect(output_wire)
        elif section[0] == 'NOT':
            input_wire = get_wire(section[1])
            output_wire = get_wire(section[3])
            node = NOTNode()
            input_wire.connect(node)
            node.connect(output_wire)
        elif section[1] == '->': # Direct assigment
            input_wire = get_wire(section[0])
            output_wire = get_wire(section[2])
            input_wire.connect(output_wire)
        else:
            raise instruction


    for signal in signals.values(): # Resolve circuit
        signal.pulse()


    for wire in wires.keys():
        print("%s -> %s" % (wire, wires.get(wire).output_signal)) # First answers
