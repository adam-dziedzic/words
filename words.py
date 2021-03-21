import nltk
import argparse


def main(args):
    text = args.text
    omit_tokens = set(args.disable_tokens + ['.', ',', ':', '-'])
    omit_pos = set(args.disable_pos)

    if text == '':
        print("Please provide text to tag. Type: python words.py 'words to "
              "be tagged'.")
        return
    tokens = nltk.word_tokenize(text)

    poss = nltk.pos_tag(tokens=tokens)
    print("token,part of speech")
    for token, pos in poss:
        # Disable output for:
        if token in omit_tokens or pos in omit_pos:
            continue
        print(f"{token},{pos}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parts of Speech')
    parser.add_argument(
        '--text', '-t',
        type=str,
        default='',
        help='The text to be tagged with parts of speech.')
    parser.add_argument(
        '--disable_pos', '-dp',
        type=str,
        nargs='+',
        default=[''],
        help='Parts of speech to be omitted.',
    )
    parser.add_argument(
        '--disable_tokens', '-dt',
        type=str,
        nargs='+',
        default=[''],
        help='Tokens to be omitted.',
    )
    args = parser.parse_args()
    main(args=args)
