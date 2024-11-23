import argparse

FILE_GENERATED_USERNAMES = 'generatedAdUsernames.txt'

def generate_ad_names(file_name:str):
    with open(file_name,mode='r')as fhr, open(FILE_GENERATED_USERNAMES,'w')as fhw:
        for line in fhr.readlines():
            fullName = line.strip()
            splittedName = fullName.split(' ')
            firstName = splittedName[0].lower()
            lastName = splittedName[1].lower()

            #first initial + last name
            fhw.write(firstName[0]+lastName+'\n')

            #first initial of last name + first name
            fhw.write(lastName[0]+firstName+'\n')

            #first name + first initial of lastname
            fhw.write(firstName+lastName[0]+'\n')

            #first name + . + first initial of lastname
            fhw.write(firstName+ "." +lastName[0]+'\n')

            #last name + . + first initial of firstname
            fhw.write(lastName+ "." +firstName[0]+'\n')

            #full name with separartors
            fhw.write(firstName+ "." +lastName+'\n')
            fhw.write(firstName+ "_" +lastName+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get the file with the names")
    parser.add_argument("file_name", type=str, help="file that contains the names to use for generation")
    args = parser.parse_args()
    generate_ad_names(file_name=args.file_name)
