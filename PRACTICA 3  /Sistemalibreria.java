import java.util.Scanner;

public class LibrarySystem {
    private Library library;

    // Constructor
    public LibrarySystem() {
        this.library = new Library();
    }

    // Method to start the menu
    public void start() {
        Scanner scanner = new Scanner(System.in);
        String option;

        do {
            System.out.println("\n--- Library Management System ---");
            System.out.println("1. Add book");
            System.out.println("2. Read book");
            System.out.println("3. Update book");
            System.out.println("4. Delete book");
            System.out.println("5. List books");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            option = scanner.nextLine();

            switch (option) {
                case "1":
                    System.out.print("Book title: ");
                    String title = scanner.nextLine();
                    System.out.print("Book author: ");
                    String author = scanner.nextLine();
                    System.out.print("Book content: ");
                    String content = scanner.nextLine();
                    Book newBook = new Book(title, author, content);
                    library.addBook(newBook);
                    break;
                case "2":
                    System.out.print("Title of the book to read: ");
                    title = scanner.nextLine();
                    library.readBook(title);
                    break;
                case "3":
                    System.out.print("Title of the book to update: ");
                    title = scanner.nextLine();
                    System.out.print("New author (leave blank to keep current): ");
                    String newAuthor = scanner.nextLine();
                    System.out.print("New content: ");
                    String newContent = scanner.nextLine();
                    
                    Book existingBook = new Book(title, "", ""); 
                    library.readBook(title); 
                    
                    if (newAuthor.isEmpty()) newAuthor = existingBook.getAuthor();
                    Book updatedBook = new Book(title, newAuthor, newContent);
                    library.updateBook(updatedBook);
                    break;
                case "4":
                    System.out.print("Title of the book to delete: ");
                    title = scanner.nextLine();
                    library.deleteBook(title);
                    break;
                case "5":
                    library.listBooks();
                    break;
                case "6":
                    System.out.println("Exiting the system...");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        } while (!option.equals("6"));

        scanner.close();
    }

    public static void main(String[] args) {
        LibrarySystem system = new LibrarySystem();
        system.start();
    }
}
