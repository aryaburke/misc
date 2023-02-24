import vcf
import sys

# to be run in the format `python3 lowercontacts.py {filename}.vcf`

contacts = sys.argv[1]

reader = vcf.Reader(filename=contacts)
writer = vcf.Writer(open('./loweredcontacts.vcf', 'w'), reader)

for contact in reader:
    print(contact)