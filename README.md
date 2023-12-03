# Apertium-based-morphological-analyzer

## Steps for MAGAHI 

1. Run help.py to write the pardefs into the magahi-dictionary.py file
2. Run the magahi-dictionary.py file, and generate file in .dix format
3. Use the auxiliary file created "another_help" to paste section data into the .dix file, or change paste data to add sections into the dictionary.py file (2nd method was giving some error)
4. Use lt-toolbox to construct morphological analyzer and generator from .dix file

## COMMAND TO CREATE MORPHOLOGICAL ANALYZER
lt-comp lr magahi-val.dix magahi_analyze.bin
Examples:   echo "kariyakko" | lt-proc magahi_analyze.bin
					echo "kariyavA" | lt-proc magahi_analyze.bin
					echo "laikino" | lt-proc magahi_analyze.bin					

## COMMAND TO CREATE MORPHOLOGICAL GENERATOR
lt-comp rl magahi-val.dix magahi_generate.bin
Examples:   echo "^kariya<adj><m><sg><p3><d>$"  | lt-proc -g magahi_generate.bin
					echo "^kariya<adj><m><sg><p3><d>$"  | lt-proc -g magahi_generate.bin
					echo "^laiki<n><f><pl><p3><o>$"  | lt-proc -g magahi_generate.bin	


## Steps for Maithili 

1. Run helper.py to write the pardefs into the maithili-dictionary.py file
2. Run the maithili-dictionary.py file, and generate file in .dix format
3. Use the auxiliary file created "another_help" to paste section data into the .dix file, or change paste data to add sections into the dictionary.py file (2nd method was giving some error)
4. Use lt-toolbox to construct morphological analyzer and generator from .dix file

## COMMAND TO CREATE MORPHOLOGICAL ANALYZER
lt-comp lr maithili-val.dix maithili_analyze.bin
Examples:   echo "ladZkian" | lt-proc maithili_analyze.bin
					echo "kaviyesaBa" | lt-proc maithili_analyze.bin

## COMMAND TO CREATE MORPHOLOGICAL GENERATOR
lt-comp rl maithili-val.dix maithili_generate.bin
Examples:   echo "^ladZki<n><f><pl><p3><o>$"  | lt-proc -g maithili_generate.bin
					echo "^kaviye<n><m><pl><p3><o>$"  | lt-proc -g maithili_generate.bin
