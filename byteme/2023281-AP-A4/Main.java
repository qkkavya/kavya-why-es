import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main{
    static ArrayList<Customer> customers=new ArrayList<>();
    File clist=new File("customers.txt");
    File h=new File(String.valueOf(Path.of("history.txt")));
    public static void main() throws IOException{
        Scanner scan=new Scanner(System.in);
        Admin.addItem(new Item("chop suey",45,"food"));
        Admin.addItem(new Item("frooti",10,"drink"));
        Admin.addItem(new Item("chole bhature",40,"food"));
        Admin.addItem(new Item("cold coffee",60,"drink")); //dummy items
        while (true){
            System.out.println("welcome to ByteMe!");
            System.out.println("1. enter as admin\n2. enter as customer\n3. exit application\n(press 1, 2 or 3)");
            int n=scan.nextInt();
            scan.nextLine();
            if (n==3){
                System.out.println("thank you for using our portal!");
                break;
            }
            else if (n==1){
                System.out.print("enter password");
                String pwd=scan.nextLine();
                if (!pwd.equals("qwer123")){
                    System.out.print("incorrect password\n");
                    continue;
                }
                else{
                    System.out.print("1. view menu\n2. add item\n3. remove item\n4. update item\n");
                    System.out.print("5. view pending orders\n6. update order status\n");
                    System.out.print("7. process refunds\n8. sales report\n9. see registered customers");
                }
                n=scan.nextInt();
                scan.nextLine();
                if (n==1){
                    System.out.println(Admin.printMenu(1,"all"));
                }
                if (n==2){
                    System.out.print("enter item name: ");
                    String name=scan.nextLine();
                    System.out.print("enter price: ");
                    int price=scan.nextInt();
                    scan.nextLine();
                    System.out.print("enter category: ");
                    String category=scan.nextLine();
                    Admin.addItem(new Item(name, price, category));
                }
                if (n==3){
                    System.out.print("enter item name: ");
                    String name=scan.nextLine();
                    Admin.removeItem(name);
                }
                if (n==4){
                    System.out.print("enter item name: ");
                    String name=scan.nextLine();
                    System.out.print("enter price: ");
                    int p=scan.nextInt();
                    scan.nextLine();
                    System.out.print("enter category: ");
                    String ca=scan.nextLine();
                    System.out.print("enter category: ");
                    boolean a=scan.nextBoolean();
                    Admin.updateItem(name, p, ca, a);
                }
                if (n==5) Admin.viewPending();
                if (n==6){
                    System.out.print("enter order id: ");
                    String name=scan.nextLine();
                    System.out.print("enter new status.\n");
                    System.out.print("(0 denotes preparing, 1 delivered/refunded, 2 out for delivery, 3 cancelled: ");
                    int p=scan.nextInt();
                    scan.nextLine();
                    Admin.updateStatus(name, p);
                }
                if (n==7){
                    System.out.print("enter order id: ");
                    String x=scan.nextLine();
                    for (Customer c:customers){
                        if (c.getCart().getClient().equals(x)){
                            c.refund();
                        }
                    }
                    Admin.updateStatus(x,3);
                }
                if (n==8){
                    Admin.report();
                }
                if (n==9){
                    System.out.println(Files.readString(Path.of("customers.txt")));
                }
            }
            else if (n==2){
                System.out.print("enter customer ID:");
                String id=scan.nextLine();
                Customer c=new Customer(1000,id);
                int choice=0;
                for (Customer i:customers){
                    if (i.getID().equals(id)){
                        c=i;
                        System.out.print("enter password");
                        String pwd=scan.nextLine();
                        if (c.login(id,pwd)){
                            choice=1;
                            List<String> k=Files.readAllLines(Path.of("C:\\Users\\viska\\Documents\\2023281-AP-A4\\2023281-AP-A4\\customers.txt"));
                            for (int m=-1;m<7;m++) System.out.println(k.get(k.indexOf(c.getID())+m));
                        }
                        else choice=2;
                    }
                }
                if (choice==0){
                    c.signup(id);
                    customers.add(c);
                    Files.write(Paths.get("C:\\Users\\viska\\Documents\\2023281-AP-A4\\2023281-AP-A4\\customers.txt"), Arrays.asList("Details: ","ID: ",c.getID(),"Balance:", c.getBalance(), "Password: ",c.getPassword(),"Address: ",c.getAddress()), StandardOpenOption.APPEND);
                    System.out.println("signed up successfully!");
                }
                if (choice==2) continue;
                System.out.print("1. view menu (by ascending price) \n2. add request\n3. become VIP\n");
                System.out.print("4. search item\n5. filter by category\n6. sort by descending price\n");
                System.out.print("7. add item\n8. change quantity\n9. remove item\n");
                System.out.print("10. view total\n11.checkout\n12. view order status\n");
                System.out.print("13. cancel order\n14. order history\n15. give review\n16.view reviews\n");
                System.out.print("Please enter your choice (1-16): ");
                choice=scan.nextInt();
                scan.nextLine();
                if (choice==1) System.out.println(Admin.printMenu(1,"all"));
                else if (choice==2){
                    System.out.print("enter request: ");
                    String req = scan.nextLine();
                    c.getCart().setRequest(req);
                }
                else if (choice==3){
                    c.setVip();
                }
                else if (choice==4){
                    System.out.print("enter item: ");
                    String item=scan.nextLine();
                    System.out.println(Admin.printMenu(1,item));
                }
                else if (choice==5){
                    System.out.print("enter category: ");
                    String cat=scan.nextLine();
                    System.out.println(Admin.printMenu(1,cat));
                }
                else if (choice==6) System.out.println(Admin.printMenu(1,"all"));
                else if (choice==7){
                    System.out.print("enter item name: ");
                    String o=scan.nextLine();
                    c.getCart().addtoCart(o);
                }
                else if (choice==8){
                    System.out.print("enter item name: ");
                    String j=scan.nextLine();
                    System.out.println("enter quantity: ");
                    int p=scan.nextInt();
                    scan.nextLine();
                    for (Item i:c.getCart().getItems()) if (i.getName().equals(j)) i.setQty(p);
                }
                else if (choice==9){
                    System.out.print("enter item name: ");
                    String z = scan.nextLine();
                    c.getCart().dropfromCart(z);
                }
                else if (choice==10){
                    System.out.println(c.getCart().getTotal());
                }
                else if (choice==11){
                    c.checkout();
                }
                else if (choice==12){
                    System.out.println(c.getCart().printStatus());
                }
                else if (choice==13){
                    Admin.updateStatus(c.getCart().getClient(), 3);
                }
                else if (choice==14){
                    c.getHistory();
                }
                else if (choice==15){
                    System.out.println("enter item: ");
                    String qw = scan.nextLine();
                    System.out.println("enter review: ");
                    String q = scan.nextLine();
                    for (Item i : c.getCart().getItems()){
                        if (i.getName().equals(qw)){
                            i.reviews.add(q);
                            break;
                        }
                    }
                }
                else if (choice==16){
                    System.out.println("enter item: ");
                    String qwe=scan.nextLine();
                    for (Item i:c.getCart().getItems()){
                        if (i.getName().equals(qwe)){
                            System.out.println(i.viewReviews());
                        }
                    }
                }
                else{
                    System.out.println("invalid choice. please select a number between 1 and 16.");
                }

            }
            else{
                System.out.println("press 1, 2 or 3");
            }
        }
        scan.close();
    }
}