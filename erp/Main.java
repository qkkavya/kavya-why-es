import java.util.Scanner;
import java.util.ArrayList;
class Main{
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        ArrayList<Student> s=new ArrayList<Student>();
        ArrayList<Prof> p=new ArrayList<Prof>();
        ArrayList<Admin> a=new ArrayList<Admin>();
        Student user=new Student("dummy");
        user.initializeCourses();
        while (true){
            user.all.get(0).daysLefttoDrop--;//for convenience of testing of this program it decrements with each iteration considered a new day
            //for the real portal, it would decrement at midnight every day instead
            System.out.println("welcome to the IIITD course registration portal!\n");
            System.out.println("1. enter\n2. exit application\n(press 1 or 2)");
            int n=scan.nextInt();
            scan.nextLine();
            if (n==2){
                System.out.println("thank you for using our portal!");
                break;
            } 
            else if (n==1){
                System.out.println("1. student/TA\n2. professor\n3. admin");
                System.out.println("4. exit application\n(press 1, 2, 3, or 4)");
                int k=scan.nextInt();
                scan.nextLine(); 
                if (k==4){
                    System.out.println("thank you for using our portal!");
                    break;
                } 
                else if (k==1){
                    System.out.print("enter email for student:");
                    String id=scan.nextLine();
                    Student student=null;
                    for (Student i:s) {
                        if (i.email.equals(id)){
                            student=i;
                            k=0;
                            System.out.print("enter password");
                            String pwd=scan.nextLine();
                            try {k=student.login(id,pwd);}
                            catch(InvalidLoginException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                        }
                    }
                    if (k==1){
                        student=new TA(id);
                        k=student.signup();
                        s.add(student);
                    }
                    if (k==0) continue;
                    System.out.println("1. view all courses\n2. register for courses\n3. drop courses");
                    System.out.println("4. view schedule\n5. track grades\n6. file complaint");
                    System.out.println("7. view complaints\n8. give feedback");
                    System.out.println("9. TA functionalities");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1) student.viewCourses();
                    else if (k==2){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter semester: ");
                        int sem=scan.nextInt();
                        scan.nextLine();
                        try {student.register(code, sem);}
                            catch(CourseFullException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                    }
                    else if (k==3){
                        System.out.print("enter course code to drop: ");
                        String code=scan.nextLine();
                        try {student.drop(code);}
                            catch(DropDeadlinePassedException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                    }
                    else if (k==4) student.viewTT();
                    else if (k==5){
                        System.out.print("grade: "+student.getGrade());
                        System.out.print("SGPA: "+student.getSGPA());
                        System.out.print("CGPA: "+student.getCGPA());
                    }
                    else if (k==6){
                        System.out.print("enter complaint: ");
                        String code=scan.nextLine();
                        student.fileComplaint(code);
                    }
                    else if (k==7) student.viewFiled();
                    else if (k==8){
                        System.out.print("enter prof email: ");
                        String code=scan.nextLine();
                        System.out.print("rate from 1 to 5 or press 0 to give descriptive feedback: ");
                        int rate=scan.nextInt();
                        scan.nextLine();
                        if (rate==0){
                            System.out.print("enter feedback: ");
                            String h=scan.nextLine();
                            student.giveFeedback(new Feedback(code,h));
                        }
                        else{
                            System.out.print("enter rating: ");
                            int feedback=scan.nextInt();
                            student.giveFeedback(new Feedback(code,feedback));
                        }
                    }
                    else if (k==9){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        for (Course course:student.all){
                            if (course.getTA().equals(id)){
                                TA t=(TA)student;
                                System.out.print("1. view student grades\n2. assign grades");
                                int x=scan.nextInt();
                                scan.nextLine();
                                if (x==1){
                                    System.out.print("enter email of student whose grade you want to view: ");
                                    String h=scan.nextLine();
                                    t.viewGrades(s,h);
                                }
                                if (x==2){
                                    System.out.print("enter email of student whose grade you want to update: ");
                                    String h=scan.nextLine();
                                    System.out.print("enter new grade: ");
                                    String i=scan.nextLine();
                                    System.out.print("enter new mark: ");
                                    int j=scan.nextInt();
                                    scan.nextLine();
                                    t.updateGrades(s,h,i,j);
                                }
                                break;
                            }
                        }
                    }
                }
                else if (k==2){
                    System.out.print("enter email for professor: ");
                    String id=scan.nextLine();
                    Prof professor=null;
                    for (Prof i:p){
                        if (i.email.equals(id)){
                            professor=i;
                            k=0;
                            System.out.print("enter password");
                            String pwd=scan.nextLine();
                            try {k=professor.login(id,pwd);}
                            catch(InvalidLoginException e){
                                System.out.println(e.getMessage());
                                continue;
                            }
                        }
                    }
                    if (k==2){
                        professor=new Prof(id);
                        k=professor.signup();
                        p.add(professor);
                    }
                    if (k==0) continue;
                    System.out.println("1. view students\n2. view courses\n3. update course details\n4. view feedback\n5. set TA");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        professor.viewStudents(code);
                    }
                    else if (k==2) professor.viewCourses();
                    else if (k==3){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter course location: ");
                        String location=scan.nextLine();
                        System.out.print("enter course timings: ");
                        String timings=scan.nextLine();
                        professor.updateCourseDetails(code, location, timings);
                    }
                    else if (k==4) professor.viewFeedback();
                    else if (k==5){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter TA email: ");
                        String l=scan.nextLine();
                        professor.assignTA(code, l);
                    }
                } 
                else if (k==3){
                    Admin admin=new Admin("admin@iiitd.ac.in");
                    System.out.print("enter password");
                    String pwd=scan.nextLine();
                    try {k=admin.login("admin@iiitd.ac.in",pwd);}
                    catch(InvalidLoginException e){
                        System.out.println(e.getMessage());
                        continue;
                    }
                    System.out.println("1. view all courses\n2. add courses\n3. delete courses");
                    System.out.println("4. view all complaints\n5.resolve complaints\n6. assign prof to course");
                    System.out.println("7. view student records\n8.update student records");
                    k=scan.nextInt();
                    scan.nextLine();
                    if (k==1) admin.viewCourses();
                    else if (k==2){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter course name: ");
                        String name=scan.nextLine();
                        System.out.print("enter semester: ");
                        int sem=scan.nextInt();
                        scan.nextLine();
                        admin.addCourses(code, name, sem);
                    }
                    else if (k==3){
                        System.out.print("enter course code to delete: ");
                        String code=scan.nextLine();
                        admin.dropCourses(code);
                    }
                    else if (k==4) admin.viewComplaints();
                    else if (k==5){
                        System.out.print("enter complaint index: ");
                        int code=scan.nextInt();
                        admin.resolveComplaint(code);
                    }
                    else if (k==6){
                        System.out.print("enter course code: ");
                        String code=scan.nextLine();
                        System.out.print("enter prof email: ");
                        String l=scan.nextLine();
                        admin.assignProf(code, l);
                    }
                    else if (k==7){
                        System.out.print("enter student email: ");
                        String email=scan.nextLine();
                        admin.viewStudentRecords(s, email);
                    }
                    else if (k==8){
                        System.out.print("enter student email: ");
                        String email=scan.nextLine();
                        System.out.print("enter grade: ");
                        String grade=scan.nextLine();
                        System.out.print("enter SGPA: ");
                        int sgpa=scan.nextInt();
                        System.out.print("enter CGPA: ");
                        int cgpa=scan.nextInt();
                        admin.updateStudentRecords(s, email, grade, sgpa, cgpa);
                    }
                } 
                else{
                    System.out.println("press 1, 2, 3, or 4");
                }
            } 
            else{
                System.out.println("Press 1 or 2");
                continue;
            }
        }
        scan.close();
    }
}