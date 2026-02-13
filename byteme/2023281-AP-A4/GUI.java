import javax.swing.*;
import java.awt.*;
import java.io.IOException;

import static java.awt.Color.*;
public class GUI{
    public static void main() throws IOException{
        Main.main();
        JFrame frame=new JFrame("ByteMe!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1200, 800);
        JLabel welcomeLabel=new JLabel("Welcome to ByteMe!", SwingConstants.CENTER);
        frame.add(welcomeLabel, BorderLayout.NORTH);
        JPanel buttonPanel=new JPanel();
        buttonPanel.setLayout(new GridLayout(3, 1, 10, 10));
        JButton adminButton = new JButton("Enter as Admin");
        JButton customerButton = new JButton("Enter as Customer");
        JButton exitButton = new JButton("Exit Application");
        buttonPanel.add(adminButton);
        buttonPanel.add(customerButton);
        buttonPanel.add(exitButton);
        frame.add(buttonPanel, BorderLayout.CENTER);
        frame.setVisible(true);
        adminButton.addActionListener(_->openAdminPanel(frame));
        customerButton.addActionListener(_->openCustomerPanel(frame));
        exitButton.addActionListener(_->System.exit(0));
    }
    private static void openAdminPanel(JFrame frame){
        String password=JOptionPane.showInputDialog(frame, "Enter Admin Password:");
        if (password==null||!password.equals("qwer123")){
            JOptionPane.showMessageDialog(frame, "Incorrect password", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        if (Admin.all.isEmpty()){
            JOptionPane.showMessageDialog(frame, "No Pending Orders", "Orders", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        StringBuilder menu=new StringBuilder("Pending orders:\n");
        int index = 1;
        for (Order entry : Admin.all){
            System.out.println(entry.getAll());
            menu.append(index).append(". ").append(entry.getClient()).append(" - ").append(entry.getAll()).append(entry.printStatus()).append(entry.getRequest()).append("\n");
            index++;
        }
        JOptionPane.showMessageDialog(frame, menu.toString(), "Orders", JOptionPane.INFORMATION_MESSAGE);
    }
    private static void openCustomerPanel(JFrame frame){
        String[] options={"View Menu (by Ascending Price)", "Search Item", "Filter by Category", "View Menu (by Descending Price)","View Reviews","Exit"};
        while (true){
            String choice=(String)JOptionPane.showInputDialog(
                    frame,
                    "Select an option:",
                    "Customer Panel",
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    options,
                    options[0]
            );
            if (choice==null||choice.equals("Exit")) break;
            switch(choice){
                case "View Menu (by Ascending Price)"->JOptionPane.showMessageDialog(frame, Admin.printMenu(1,"all"), "Menu", JOptionPane.INFORMATION_MESSAGE);
                case "Search Item"->{
                    String item=JOptionPane.showInputDialog(frame, "Enter item name:");
                    if (item!=null){
                        JOptionPane.showMessageDialog(frame, Admin.printMenu(1, item), "Search Results", JOptionPane.INFORMATION_MESSAGE);
                    }
                }
                case "Filter by Category"->{
                    String category=JOptionPane.showInputDialog(frame, "Enter category:");
                    if (category!=null){
                        JOptionPane.showMessageDialog(frame, Admin.printMenu(1, category), "Search Results", JOptionPane.INFORMATION_MESSAGE);
                    }
                }
                case "View Menu (by Descending Price)"->JOptionPane.showMessageDialog(frame, Admin.printMenu(6,"all"), "Menu", JOptionPane.INFORMATION_MESSAGE);
                case "View Reviews"-> {
                    String item = JOptionPane.showInputDialog(frame, "Enter item name:");
                    for (Item i: Admin.menu.values()){
                        if (item.equals(i.getName())) JOptionPane.showMessageDialog(frame, i.viewReviews(), "Search Results", JOptionPane.INFORMATION_MESSAGE);
                    }
                }
                default->JOptionPane.showMessageDialog(frame, "Invalid choice. Please select a valid option.");
            }
        }
    }
}
