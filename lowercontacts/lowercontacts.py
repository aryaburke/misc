import vcfpy
import sys

reader = vcfpy.Reader.from_path(sys.argv[1])
writer = vcfpy.Writer.from_path('/dev/stdout', reader.header)

print(reader)
for contact in reader:
    print(contact)