package com.mesonet.Backend;

import org.springframework.core.io.ClassPathResource;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PlaceholderScript {

    public String data(){
        List<String> dataList = new ArrayList<>();
        try {
            Scanner fileScanner = new Scanner(new ClassPathResource("data.csv").getFile());
//            ArrayList<String> data = new ArrayList<>();
            int counter = 0;
            String line = "";

            while (fileScanner.hasNext() && counter < 25) {
                line = fileScanner.nextLine();

                if (counter >= 4) {
                    String[] cell = line.split(",");
                    dataList.add(cell[16]);
                }

                counter ++;
            }

            fileScanner.close();

            for (String data : dataList){
                System.out.println(data);
            }

//            Scanner lineScanner = new Scanner(line);
//            lineScanner.useDelimiter(",");
//            while (lineScanner.hasNext()) {
//                String dataCell = lineScanner.next();
//                data.add(dataCell);
//            }
//            lineScanner.close();
//
//            return data.get(0);

            return "hi";
        } catch (IOException e) {
            System.out.println("File not found");
        }
        return "0";
    }

    public static void main(String[] args){
        new PlaceholderScript().data();
    }
}


