def find_unique_indexes(strings):
    """
    Finds the indexes of the first unique character in each of the strings.

    Args:
        strings (list): A list of strings to search for unique characters in.

    Returns:
        A list of integers representing the indexes of the first unique character in each string.
    """
    for i in range(len(strings[0])):
        unique_index = -1
        # Collect all characters at the i-th index from all strings
        chars = [s[i:i+4] for s in strings]

        # Check if any character appears more than once
        if sum(chars.count(c) > 1 for c in chars) == 0:
            unique_index = i
            print([s[i:i+4] for s in strings])
            break

    return unique_index

strings = ["""1 cctttattta ctatttggtg cttgagctgg aatagtggga acggctttaa gcctgctaat
61 tcgagcagag ctaaaccaac caggcagcct ccttggcgac gaccagatct ataatgtcat
121 cgttacagca catgcatttg taataatttt ttttatggtc atacccgcta taattggggg
181 atttggaaac tgactaattc ctctaataat cggggccccc gacatggcat tcccccgaat
241 gaataacata agcttttgac ttctccctcc ctcccttctc cttcttctag catccgctgg
301 ggtagaagct ggggccggaa ctggatgaac agtttaccca cccctagcgg gtaatctagc
361 acatgcgggc gcatccgtag atttaaccat cttctccctt catttagcag gagtttcctc
421 aattctgggg gctattaatt ttatcacaac gatcatcaat atgaagcctc ctgctatctc
481 tcagtatcaa acacccctat ttgtctgagc agtattaatc acagcagtcc tactacttct
541 ttctcttcca gttcttgctg caggtattac aatactctta acagaccgaa atttaaacac
601 caccttcttc gaccctgcag gagggggaga cccaattctt taccaacact tattc""", 

"""1 cctctattta ctatttggtg cttgagccgg aatggtaggc actgctttga gcctactaat
61 tcgagccgag ctaaatcaac cgggcagcct tctcggagac gaccagatct acaatgttat
121 cgttacagca cacgcattcg taataatttt ttttatggtg atgcccgcca tgatcggagg
181 ctttggaaat tgattagtcc cactaataat tggagcccca gacatagcat ttcctcgaat
241 aaataatata agcttttgac tcctgccccc ttctcttctt cttctccttg cttccgccgg
301 ggtagaggcc ggagctggaa ctgggtgaac agtttacccg cccctagctg gcaatctagc
361 ccacgcagga gcatccgtag acctgaccat cttctccctc cacctggccg gaatctcctc
421 aattctaggg gctattaact ttatcacaac cattattaac ataaaacccc ctgctatttc
481 acaataccaa actccactat ttgtgtgagc tgtcctaatt actgcagtgc tacttctgct
541 ttctctcccc gtccttgctg ccggcatcac aatgcttctt acagaccgaa atcttaatac
601 tactttcttt gaccctgcag gagggggaga cccaattctt taccagcact tg""",

"""1 tctctatcta gtattcggtg cttgagctgg gatagtaggc accgccttaa gtctgctcat
61 ccgagcagag ctcagccagc caggcaccct cctaggcgac gatcagattt ataatgtaat
121 cgttacggca catgcgttcg taatgatttt ctttatagta ataccaatta tgattggggg
181 atttgggaat tgactaattc ccttaatgat tggggctccg gacatggcct tccctcgaat
241 gaataacata agcttttgac tcctccctcc atcctttttc ctgcttcttg cctcttctgg
301 cgtagagtcc ggggccggca ctggatgaac agtttatcct ccactagccg gtaatctagc
361 ccatgccgga gcatccgttg atctaactat cttctccctt caccttgcag ggatctcctc
421 cattcttggg gctatcaatt ttattacaac aatcctcaac atgaaacccc ctgctatgtc
481 ccagtatcaa actccccttt tcgtctgatc tgttctaatt acagccgttt tacttctctt
541 gtccctcccc gttcttgcag ccggaattac aatgcttctt acagaccgaa accttaatac
601 aaccttcttt gaccctgcag ggggcggcga ccccattctt taccaacacc tgttc""",

"""1 cctttattta gtttttggtg cttgagctgg gatagtagga acggccctaa gcctcctaat
61 ccgggcagaa ttaagccaac caggcgccct cctcggagat gatcaaattt ataatgtaat
121 tgttacagca cacgcattcg taataatttt ctttatagta ataccaatta tgattggtgg
181 gttcggaaat tgattaattc cactaatgat tggagcccct gacatagcat tcccacgaat
241 aaataacata agcttttgac ttttaccacc atctttcctg cttctacttg catcctctgc
301 agtagaatct ggtgcaggca caggatgaac agtatacccc cctctagccg gtaatcttgc
361 acatgcagga gcatccgtag atctcactat tttctccctc cacctagcag ggatttcttc
421 aattcttgga gctattaatt ttattacaac aattattaat atgaaacctc ctgctatttc
481 ccaatatcaa acccccctgt ttgtatgagc agtactaatt accgccgttc tactccttct
541 ctcacttcct gttctcgctg ctggaattac aatactactc acagatcgaa acctgaatac
601 cactttcttt gacccagcag gtggaggaga ccccatttta tatcaacatt ta""",

"""1 cctttatcta gtatttggtg cctgggccgg aatagtaggc acggccctaa gcctgctcat
61 tcgagcagaa ctaagccagc caggagctct tcttggagac gaccagattt ataatgtaat
121 tgttacagcg catgcatttg taataatttt ctttatagta ataccaatca tgatcggagg
181 attcgggaac tgactgatcc cactaatgat cggggccccc gatatggcat tccctcgaat
241 aaataacatg agcttttgac tcctcccgcc atcattccta ttgctactcg cctcttctgg
301 ggtagaagcc ggtgctggaa ctgggtgaac agtttaccct cccctagcag gaaacctagc
361 acacgcagga gcatctgtag acctaactat tttctccctg catctagcag gtgtttcctc
421 aattctggga gcaatcaact tcattacaac aatcatcaac atgaaacctc ctgccatttc
481 ccagtatcaa acgcccctat tcgtctgagc cgtcctaatt actgctgttc tacttcttct
541 ctccctacca gttttagcgg ccggaattac aatgcttctt acagaccgaa atctaaacac
601 aaccttcttt gacccagcag gaggagggga tcccatcctc taccaacatc tg""",

"""1 cctctatcta gtatttggtg cttgagctgg aatagtagga acagccctga gcctccttat
61 tcgagcagaa ctaagccaac caggcgctct cctcggagac gaccagattt acaacgtaat
121 tgttacggca catgcctttg taataatttt ctttatagta ataccaatta taattggagg
181 gtttggaaac tgacttatcc cactaatgat cggtgcccct gatatggcat tcccccgaat
241 gaacaatatg agcttctgac ttcttccccc atcgttccta cttcttcttg cctcctccgg
301 agttgaagca ggtgcaggaa caggctgaac tgtctaccca ccactatcag gcaacctagc
361 tcacgcagga gcttctgttg acttaactat tttctccctc cacttagcag gtgtgtcctc
421 aattttagga gccattaatt ttattaccac tattattaat atgaaacctc cagctatttc
481 tcaataccag actcctctct tcgtatgagc cgtactcatc acggccgtgc tcctccttct
541 gtcccttcct gttttagccg ctggaattac gatacttcta accgaccgaa acttaaatac
601 cacattcttc gacccagctg gaggaggaga ccccattctt taccaacatt tattc""",

"""1 cctttatctt gtatttggtg cctgggctgg gatagtagga acagccctta gcctactaat
61 tcgggctgag ctaagccagc caggggctct actgggcgat gaccagatct ataatgtaat
121 tgttacagca catgcttttg taataatctt tttcatagta atgccaatca tgattggtgg
181 ctttggaaat tgacttgtcc cacttataat cggcgcccct gacatagcat tccctcgaat
241 aaataacata agcttctgac ttctcccccc ttctttcctg ctccttcttg cctcttcggg
301 ggtagaagct ggtgccggta ctggttgaac ggtctacccg cccctagccg gaaatttagc
361 ccatgcagga gcatccgtag acttaactat tttctcactt catttagcag gtatctcatc
421 aattctaggt gcaattaact ttattacaac cattattaac ataaaacccc ctgccatctc
481 ccaataccaa acacctttgt ttgtgtgagc tgtactaatc acagcagtac tactactcct
541 ctcccttccc gtccttgccg ccggcatcac catgttgctc actgatcgta accttaacac
601 taccttcttt gacccagccg gaggaggaga tcca""",

"""1 cctctatctt gtgttcggcg catgagccgg gatagtaggg acagccctaa gcctgctcat
61 ccgagcagag ttaagccagc ccggcgccct ccttggggac gatcagattt ataacgttat
121 cgttacagcc cacgcattcg tcataatttt ctttatagta ataccaatta tgattggagg
181 cttcggaaac tgactaattc ccctaatgat tggggcccct gacatggcct tccctcggat
241 gaacaatata agcttctgac ttcttccacc ctcattcctt cttcttctcg cctcctctgg
301 cgttgaggca ggggccggaa ctggttggac agtctaccca cccctagcag ggaaccttgc
361 ccatgctggt gcatccgttg accttactat tttttcactt cacttggcag ggatttcatc
421 aattctaggt gcaatcaact tcatcacaac cattattaat atgaaacccc cagccatctc
481 ccaatatcaa acgcctcttt tcgtatgggc tgttctcatt acggcagtcc ttctcctcct
541 ctcgctccca gtccttgccg ctggtattac aatgctctta acagaccgaa atcttaacac
601 cactttcttc gaccctgctg gaggggggga cccaattctt taccaacacc tg""",

"""1 cctttacctt gtatttggtg cctgagccgg aatagtaggc actgccttaa gccttctcat
61 ccgagctgaa ctaagtcaac ccggggccct tctcggagac gaccagattt ataatgttat
121 cgttacagct catgcatttg taatgatctt ttttatagtc atgcctatca taatcggagg
181 cttcgggaac tgactcatcc ccctcatgat tggggcacct gacatggcct tccctcgaat
241 gaacaatatg agcttctgac ttcttcctcc ctccttcctc ctattactcg cctcctctgg
301 cgtagaagcg ggagcaggta ccggatgaac cgtttacccc cctctagcag gaaatcttgc
361 acacgcaggt gcatccgtcg acctaacaat tttctctctt catctagcag gaatttcttc
421 tatcctagga gcaattaact ttattacaac aatcgttaac ataaaaccgc ctgccatctc
481 ccaataccaa accccgctgt tcgtatgagc tgttttaatt actgccgtac ttcttctcct
541 ctcactccct gtcctcgctg caggaatcac aatgcttctc acagatcgaa atctaaacac
601 gaccttcttt gaccctgcag gcggaggana cccaattctt tatcaacacc tg""",

"""1 cctttatcta gtatttggtg cctgagccgg aatagtagga acagctctaa gtctcctcat
61 tcgggcagaa ctaagccaac ccggcgctct ccttggagac gaccaaattt ataatgtaat
121 tgttacggca cacgcctttg taataatctt ctttatagta ataccaatca tgattggagg
181 cttcggaaac tgacttattc ccctaatgat cggggccccc gacatggcct ttccccgaat
241 aaacaatata agcttctgac ttctcccccc ttcctttctt cttctgcttg cctcttcagg
301 tgtagaagca ggtgcaggaa caggatgaac agtctaccct ccactatctg gcaacctagc
361 tcatgcaggg gcctccgttg acctaaccat tttctccctt catctagcag gaatttcatc
421 gatcctagga gcaatcaact ttatcactac tattattaac atgaagcccc cttctatctc
481 tcaataccaa acccctctct ttgtatgagc agttctaatc accgccgtac tactactcct
541 ctcccttccc gtcttagctg ccggtattac tatgctccta acggaccgaa accttaatac
601 tactttcttt gaccctgcag gaggaggaga cccaatcctt taccaacacc tt"""]
unique_indexes = find_unique_indexes(strings)
print(unique_indexes)

