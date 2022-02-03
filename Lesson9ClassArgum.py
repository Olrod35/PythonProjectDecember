def parse_args():
#     import argparse
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("square", type=int,
#                         help="display a square of a given number")
#     parser.add_argument("-v", "--verbose", action="store_true",
#                         help="increase output verbosity")
#     parser.add_argument("-n", action="store", help='Variable N')
#     parser.add_argument("-l", action="append", help='List')
#     parser.add_argument("--const", action="store_const", const=5, help='List')
#     return parser.parse_args()
#
#
# if __name__ == "__main__":
#     params = parse_args()
#     print(params)
#     # breakpoint()
#     answer = params.square ** 2
#     if params.verbose:
#         print("the square of {} equals {}".format(params.square, answer))
#     else:
#         print(answer)


    # import argparse
    #
    # def parent():
    #     parent_parser = argparse.ArgumentParser(add_help=False)
    #     parent_parser.add_argument('--user', action="store")
    #     parent_parser.add_argument('--password', action="store")
    #     return parent_parser
    #
    # def child(parent_parser):
    #     child_parser = argparse.ArgumentParser(parents=[parent_parser])
    #     child_parser.add_argument('--show_all', action="store_true")
    #     return child_parser
    #
    # p = parent()
    # args = p.parse_args()
    # if args.user == 'super':
    #     c = child(p)
    #     args = c.parse_args()
    #
    # print(args)
© 2022 GitHub, Inc.
Terms
Privacy
Secu