#include <iostream>
#include <string>

class Book {
    private:
        int rating;
    public:
        std::string title;
        std::string author;
        int noPages;
        Book(){
            title="no title";
            author= "unknown";
            noPages=0;
            setRating(0);
        }
        Book(std::string name, std::string theauthor, int pages, int stars){
            title = name;
            author = theauthor;
            noPages = pages;
            setRating(stars);
            std::cout<<"this is the constructor for "<<title<<std::endl;
        }
        bool isGood(){
            if (rating>6){
                return true;
            }
            return false;
        }
        void setRating(int r){
            if (r>=0 and r<=10){
                rating = r;
            }
            else{
                std::cout<<"Invalid Rating\n";
                rating=0;
            }
        }
        int getRating(){
            return rating;
        }
};

class Novel : public Book{
    std::string genre;
    public:
        Novel(){
            title="no title";
            author= "unknown";
            noPages=0;
            setRating(0);
            genre = "unspecified";
        }
        Novel(std::string name, std::string theauthor, int pages, int stars, std::string type){
            title = name;
            author = theauthor;
            noPages = pages;
            setRating(stars);
            genre = type;
            std::cout<<"this is the constructor for "<<title<<std::endl;
        }
};

int main(){
 
    Book book1;
    book1.title = "Harry Potter";
    book1.author = "J.K. Rowling";
    book1.noPages = 500;

    Book book2("LOTR","Tolkein",700,8);
    std::cout<< book2.isGood() <<std::endl;

    Book book3;
    std::cout<< book3.title <<std::endl;

    Novel novel2("Wuthering Heights","Bronte",400,9,"Young Adult");
    std::cout<< novel2.isGood() <<std::endl;

    Novel novel1;
    std::cout<< novel1.title;

    
    return 0;
}
