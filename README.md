# Parts of speech for tokens.

These are the instructions. If you have any problems, please let me know. 

1. Install Python 3 on Mac: 

Check first this: https://docs.python-guide.org/starting/install3/osx/ 
If you have python 3 then stop here. 
Otherwise follow these steps: https://docs.python.org/3/using/mac.html  

2. Open the terminal and create the directory code: `mkdir code`. Go to the new directory: `cd code`.
3. Download my code: `git clone https://github.com/adam-dziedzic/words.git` and go to the code: `cd words`
4. Install libraries: `pip install nltk`
5. Execute: `python download.py`
6. Try the program: `python words.py -t "This is an example of a text.`
Output:
```
token,part of speech
This,DT
is,VBZ
an,DT
example,NN
of,IN
a,DT
text,NN
```

7. License: NLTK library has Apache 2.0 License: https://github.com/nltk/nltk/blob/develop/LICENSE.txt

8. Help:

```
python words.py -h
usage: words.py [-h] [--text TEXT] [--disable_pos DISABLE_POS [DISABLE_POS ...]] [--disable_tokens DISABLE_TOKENS [DISABLE_TOKENS ...]]

Parts of Speech

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  The text to be tagged with parts of speech.
  --disable_pos DISABLE_POS [DISABLE_POS ...], -dp DISABLE_POS [DISABLE_POS ...]
                        Parts of speech to be omitted.
  --disable_tokens DISABLE_TOKENS [DISABLE_TOKENS ...], -dt DISABLE_TOKENS [DISABLE_TOKENS ...]
                        Tokens to be omitted.
```

### The list of parts of speech (POS) tags is as follows, with examples of what each POS stands for.
```
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
```
Please see: http://bit.ly/3f0eZIv
