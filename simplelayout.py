import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description="simpleLayout-CLI Project")
    parser.add_argument("--board_grid", type=int, help="布局板分辨率")
    parser.add_argument("--unit_grid", type=int, help="矩形组件分辨率")
    parser.add_argument("--unit_n", type=int, help="组件数")
    parser.add_argument("--positions", nargs='+', type=int, help="位置")
    parser.add_argument("--outdir", default="example-dir", help="输出结果的目录")
    parser.add_argument("--file_name", default="example", help="输出文件名")
    args = parser.parse_args()

    if args.board_grid % args.unit_grid != 0:
        sys.exit(0)
    if (
        args.positions[0] != 1
        or len(args.positions) != args.unit_n
        or max(args.positions) > (args.board_grid / args.unit_grid) ** 2
    ):
        sys.exit(0)
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    with open(args.outdir + '/' + args.file_name + '.jpg', 'w') as f:
        f.write("")
    with open(args.outdir + '/' + args.file_name + '.mat', 'w') as f:
        f.write("")


if __name__ == "__main__":
    main()
