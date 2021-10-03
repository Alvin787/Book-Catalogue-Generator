from Book_Class import *
import csv

def read_file(filename):
    book_dict={}
    with open(filename, "r", encoding='utf-8', errors='ignore') as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)
        for line in reader:
            category_list=[]
            category_filter=line[2].split(';')
            author_list=line[0].split(';')
            average_rating=float(line[17])
            
            for i in category_filter:
                if i not in category_list:
                    category_list.append(i)

            isbn_number = line[13]
            if isbn_number == '':
                isbn_number = None
            else:
                isbn_number = int(isbn_number)
            
            book_instance=Book(line[19], author_list, category_list, line[3], line[7], isbn_number, line[14], line[15], average_rating, int(line[18]))
        
            if category_list[0] not in book_dict:
                book_dict[category_list[0]] = {}
                
            if average_rating not in book_dict[category_list[0]]:
                book_dict[category_list[0]][average_rating]=[]
                
            book_dict[category_list[0]][average_rating].append(book_instance)
    return book_dict

def generate_index_file(dataset, filename):
    with open(filename, "w", encoding='utf-8', errors='replace', newline='') as fileout:
        writer = csv.writer(fileout)
        writer.writerow(['ISBN 13','Title','Author','Category','Format','Language','Rating Avg'])
        for category in dataset:
            for rating in dataset[category]:
                for book in dataset[category][rating]:
                    first_category = book.categories()[0]
                    authors = ''
                    for i in book.author():
                        if len(book.author())==1:
                            authors+=i
                        elif i==book.author()[-1]:
                            authors+=i
                        else:
                            authors+=i+'     '
                    index_text=[book.isbn_13(),book.title(),authors,first_category,book.book_format(),book.language(),book.rating_avg()]
                    writer.writerow(index_text)

def generate_book_detail_file(dataset, filename):
    with open(filename, "w", encoding='utf-8', errors='replace', newline='') as fileout:
        for category in dataset:
            for rating in dataset[category]:
                for book in dataset[category][rating]:
                    fileout.write(book.title()+'\n')

                    author_detail=''
                    for i in book.author():
                        if len(book.author())==1:
                            author_detail+=i
                        elif i==book.author()[-1]:
                            author_detail+=i
                        else:
                            author_detail+=i+'     '
                    
                    fileout.write(f'by: {author_detail}'+'\n\n')
                    fileout.write(f'{book.book_format()} | {book.language()} | published: {book.publication_date()}'+'\n')
                    fileout.write(f'average rating: {book.rating_avg()} for {book.rating_count()} ratings'+'\n\n')
    
                    fileout.write('Categories\n')
                    for i in book.categories():
                        fileout.write(i+'\n')
                    fileout.write('\n')

                    fileout.write('Description'+'\n')
                    fileout.write(book.description()+'\n')
                    fileout.write(f'ISBN: {book.isbn_13()}'+'\n\n')

#MAIN
dataset = read_file("book_dataset.csv")
generate_index_file(dataset, "Book_Index.csv")
generate_book_detail_file(dataset, "Book_Details.txt")













