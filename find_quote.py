from models import Quotes, Authors
import connect

Quotes
def find_by_name(args):
    author = Authors.objects(fullname=args).get()
    quotes = Quotes.objects(author=author)
    quotes_list = []
    for q in quotes:
        quotes_list.append(q.quote)
    return quotes_list

def find_by_tag(args):
    quotes = Quotes.objects(tags__name=args)
    quotes_list = []
    for q in quotes:
        quotes_list.append(q.quote)
    return quotes_list

def find_by_tags(args):
    quotes = Quotes.objects(__raw__={"tags.name":{"$all":args.split()}})
    quotes_list = []
    for q in quotes:
        quotes_list.append(q.quote)
    return quotes_list

commands = {
    "name": find_by_name,
    "tag": find_by_tag,
    "tags": find_by_tags
    }

def parse(command):
    func, arguments = command.split(":")
    return (commands[func], arguments.strip()) 

def print_quotes(quotes):
    if not quotes:
        print("Quotes not found")
    for q in quotes:
        print(q)

def main():
    while True:
        command = input()
        if command == "exit":
            return
        data = parse(command)
        try:
            print_quotes(data[0](data[1]))
        except:
            print("Quotes not found")

main()

#print('--- All notes ---')
#quotes = Notes.objects()
#for note in notes:
#    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
#    tags = [tag.name for tag in note.tags]
#    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

#print('--- Notes with tag Fun ---')

#notes = Notes.objects(tags__name='Fun')
#for note in notes:
#    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
#    tags = [tag.name for tag in note.tags]
#    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")
