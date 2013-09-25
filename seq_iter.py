
def give_dna_stats(seqs):
  fh = open('fasta.fas', 'r')
  line = fh.readline()
  sequence_counter = 0
  while line != '':
    line = line.rstrip()
    if line.startswith('>'):
      print 'The name of the sequence is ' + line
    else:
      line = line.upper()
      gc_count = float(line.count('G') + line.count('C'))/len
      n_count = line.count('N')
      print 'GC-content is ' +  str(gc_count)
      print 'There are ' + str(n_count)  + ' Ns.'
      sequence_counter += 1
    line = fh.readline()
  print 'There are ' + str(sequence_counter) + ' sequences in the file.'
  
give_dna_stats('fasta.fas')


