import pytest

from ccheck.utils.tokenizer.tokenizer import Tokenizer

def test_code():
    tokenizer = Tokenizer()

    output = tokenizer.tokenize('#include')

    assert tokenizer.tokenize('#include') == 'directive'
