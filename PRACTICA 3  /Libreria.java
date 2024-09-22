import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Library {
    public void addBook(Book book) {
        try {
            File file = new File(book.getTitle() + ".txt");
            if (file.createNewFile()) {
                FileWriter writer = new FileWriter(file);
                writer.write(book.toString());
                writer.close();
                System.out.println("Book '" + book.getTitle() + "' added successfully.");
            } else {
                System.out.println("The book already exists.");
            }
        } catch (IOException e) {
            System.out.println("Error adding the book.");
            e.printStackTrace();
        }
    }

    public void readBook(String title) {
        try {
            File file = new File(title + ".txt");
            if (file.exists()) {
                Scanner reader = new Scanner(file);
                while (reader.hasNextLine()) {
                    System.out.println(reader.nextLine());
                }
                reader.close();
            } else {
                System.out.println("The book does not exist.");
            }
        } catch (IOException e) {
            System.out.println("Error reading the book.");
            e.printStackTrace();
        }
    }

    public void updateBook(Book book) {
        try {
            File file = new File(book.getTitle() + ".txt");
            if (file.exists()) {
                FileWriter writer = new FileWriter(file, false);
                writer.write(book.toString());
                writer.close();
                System.out.println("The book '" + book.getTitle() + "' has been updated.");
            } else {
                System.out.println("The book does not exist.");
            }
        } catch (IOException e) {
            System.out.println("Error updating the book.");
            e.printStackTrace();
        }
    }

    public void deleteBook(String title) {
        File file = new File(title + ".txt");
        if (file.exists()) {
            if (file.delete()) {
                System.out.println("The book '" + title + "' has been deleted.");
            } else {
                System.out.println("Could not delete the book.");
            }
        } else {
            System.out.println("The book does not exist.");
        }
    }

    public void listBooks() {
        File directory = new File(".");
        File[] files = directory.listFiles((dir, name) -> name.endsWith(".txt"));

        System.out.println("Available books in the library:");
        if (files != null && files.length > 0) {
            for (File file : files) {
                System.out.println("- " + file.getName().replace(".txt", ""));
            }
        } else {
            System.out.println("No books available.");
        }
    }
}
