package com.mesonet.Backend.Controller;

import java.util.*;
import java.io.*;

import org.springframework.core.io.ClassPathResource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class DataController {

   private Map<String, Integer> dataMap = new HashMap<>(){{
       put("TIMESTAMP", 0);
       put("RECORD", 1);
       put("BATT_V_AVG", 2);
       put("WS_30FT_MPH_AVG", 3);
       put("WS_30FT_MPH_MAX", 4);
       put("WINDDIR_30FT_D1_WVT", 5);
       put("WINDDIR_30FT_SD1_WVT", 6);
       put("WS_10FT_MPH_AVG", 7);
       put("WS_10FT_MPH_MAX", 8);
       put("WINDDIR_10FT_D1_WVT", 9);
       put("WINDDIR_10FT_SD1_WVT", 10);
       put("WS_SONIC_MPH_AVG", 11);
       put("WS_SONIC_MPH_MAX", 12);
       put("WINDDIR_SONIC_D1_WVT", 13);
       put("WINDDIR_SONIC_SD1_WVT", 14);
       put("AIR_TF_AVG", 15);
       put("RH_AVG", 16);
       put("SLRW_AVG", 17);
       put("SLR_MJ_TOT", 18);
       put("DEWPT_F", 19);
       put("RAINSINCEMIDNIGHT", 20);
       put("RV_PRE_ACCU_TOT", 21);
       put("RV_TIPS_TOT", 22);
       put("RV_TOT_PRE_ACCU", 23);
       put("RV_AVG_PRE_INT_MAX", 24);
       put("RV_MAX_PRE_INT_MAX", 25);
       put("VWC_5CM_AVG", 26);
       put("KA_5CM_AVG", 27);
       put("SOILTMPF_5CM_AVG", 28);
       put("BULKEC_5CM_AVG", 29);
       put("VWC_10CM_AVG", 30);
       put("KA_10CM_AVG", 31);
       put("SOILTMPF_10CM_AVG", 32);
       put("BULKEC_10CM_AVG", 33);
       put("VWC_20CM_AVG", 34);
       put("KA_20CM_AVG", 35);
       put("SOILTMPF_20CM_AVG", 36);
       put("BULKEC_20CM_AVG", 37);
       put("VWC_30CM_AVG", 38);
       put("KA_30CM_AVG", 39);
       put("SOILTMPF_30CM_AVG", 40);
       put("BULKEC_30CM_AVG", 41);
       put("VWC_40CM_AVG", 42);
       put("KA_40CM_AVG", 43);
       put("SOILTMPF_40CM_AVG", 44);
       put("BULKEC_40CM_AVG", 45);
       put("VWC_50CM_AVG", 46);
       put("KA_50CM_AVG", 47);
       put("SOILTMPF_50CM_AVG", 48);
       put("BULKEC_50CM_AVG", 49);
       put("T109_30FT_F_AVG", 50);
       put("T109_10FT_F_AVG", 51);
       put("ABSBARO_INHG_AVG", 52);
       put("SEALVL_BARO_INHG_AVG", 53);
       put("HEATINDX_TMPF_AVG", 54);
       put("WINDCHILL_TMPF_AVG", 55);
       put("BATTERYVOLTAGE", 56);
       put("BATTERYCURRENT", 57);
       put("LOADCURRENT", 58);
       put("CHARGEINPUTVOLTAGE", 59);
       put("CHARGEINPUTCURRENT", 60);
       put("CHARGETEMP", 61);
       put("CHG_STATE", 62);
       put("CHG_SOURCE", 63);
       put("CK_BATT", 64);
   }};

    public List<String[]> data(int column) throws Exception{
        List<String[]> dataList = new ArrayList<>();
        try {
	    Scanner fileScanner = new Scanner(new ClassPathResource("data.csv").getFile());
            int counter = 0;
            String line = "";

             while (fileScanner.hasNext() && counter < 25) {
                line = fileScanner.nextLine();

                if (column > line.length()){
                    throw new Exception("Column number is too high");
                } else if (column < 0) {
                    throw new Exception("Column number is too low");
                }

                if (counter >= 4) {
                    String[] cell = line.split(",");
                    dataList.add(new String[]{cell[0].replace("\"", ""), cell[column]});
                }

                counter ++;
            }

            fileScanner.close();

            return dataList;
        } catch (IOException e) {
            throw new Exception("File not found");
        }
    }

    @GetMapping("/get-data")
    public ResponseEntity<List<String[]>> data(@RequestParam String type){
        try{
            List<String[]> dataList = data(dataMap.get(type.toUpperCase()));
            return new ResponseEntity<>(dataList, HttpStatus.OK);
        } catch (Exception e){
	    System.out.println(e);
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping("/")
    public String hello(){
        return "Hello World!";
    }
}


