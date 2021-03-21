import nltk
from nltk.tag.perceptron import PerceptronTagger

download = False

if download:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')


class PerceptronTagger2(PerceptronTagger):

    def __init__(self, load=True):
        super(PerceptronTagger2, self).__init__(load=load)

    def tag(self, tokens, return_conf=False, use_tagdict=True):
        '''
        Tag tokenized sentences.
        :params tokens: list of word
        :type tokens: list(str)
        '''
        prev, prev2 = self.START
        output = []

        context = self.START + [self.normalize(w) for w in tokens] + self.END
        for i, word in enumerate(tokens):
            tag = self.tagdict.get(word)
            if not tag:
                features = self._get_features(i, word, context, prev, prev2)
                tag = self.model.predict(features)
            output.append((word, tag))
            prev2 = prev
            prev = tag

        return output


def main():
    tokens = nltk.word_tokenize(
        "Can you please buy me an Arizona Ice Tea? It's $0.99.")
    print('Tokens: ', tokens)

    pos = nltk.pos_tag(tokens=tokens)
    print('pos: ', pos)

    pos_table = nltk.pos_tag(['can'])
    print('pos_table: ', pos_table)

    pt = PerceptronTagger2()

    tags = pt.tag(['can'])
    print('tags: ', tags)


if __name__ == "__main__":
    main()
