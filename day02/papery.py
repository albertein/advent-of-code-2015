import sys


def calc_paper(data):
    paper = 0
    ribbon = 0
    for l, w, h in data:
        faces = [l * w, l * h, w * h]
        paper += sum([2 * face for face in faces])
        paper += min(faces)

        ribbon += sum([2 * side for side in sorted([l, w, h])[:2] ])
        ribbon += l * w * h

    return paper, ribbon

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    data = [[int(x) for x in line.split('x')] for line in input_file]
    print(calc_paper(data))
