/*

30 seemed to be a good length for most names/titles

*/

#define STR 30

/*

Books must have an author, title, and bookId.

Added a bool to track if the book is being borrowed or not.

Decided not to implement a way to check how long a book is being borrowed (AKA: No late penalty).

*/

typedef struct Book{

    char author[STR];
    char title[STR];
    int* bookId;
    bool* inLibrary;
    book* next;
    book* prev;

} book;

/*

Members have a first and last name as well as an Id.

Members can only borrow so many books at once which 
I track through bookCount.

*/
typedef struct Member{

    char firstName[STR];
    char lastName[STR];
    int* memberId;
    int* bookCount;
    member* next;
    member* prev;

} member;

/*

Below are two separate double linked lists for books and members.

Since there is no inheritance in C I was unsure on how to use 
the same list structure for both books and members.

Just simple structure for double linked list.

The book and member structs are the same as a node struct.

*/
typedef struct BookList{

    book* node;
    book* head;
    book* tail;

} bookList;

typedef struct MemberList{

    member* node;
    member* head;
    member* tail;

} memberList;
