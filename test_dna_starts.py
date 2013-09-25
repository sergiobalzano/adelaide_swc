#Test dna_starts_with

def dna_starts_with(dnastring1, dnastring2):
 return dnastring1[0:len(dnastring2)]==dnastring2

import math
def test_dna_starts_with_single():
 if len(dna_starts_with('atgc', 'a')) == 1:
  raise ValueError('the second DNA string must be longer than 1 bp ') 
 
def test_dna_starts_with_bigger():
 if len(dna_starts_with('atgc','aatga'))==1:
  raise ValueError('the second DNA string must not be longer than the first one ')

def test_dna_starts_with_itself():
 if dna_starts_with('atgc','atgc')==1:
  raise ValueError('the two DNA strings must not be the same') 

test_dna_starts_with_single()
test_dna_starts_with_bigger()
test_dna_starts_with__itself()
