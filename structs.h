#define STR 30

typedef struct Book{

    char author[STR];
    char title[STR];
    int *bookId;

} book;

typedef struct Member{

    char firstName[STR];
    char lastName[STR];
    int *memberId;

} member;
