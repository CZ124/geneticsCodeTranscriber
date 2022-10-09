# Hashmap

- stores items in key/value pairs
- one object is the key of another object
- ```HashMap<String, String> capitalCities = new HashMap<String, String>();```
  - String can be replaced with the ```type``` desired
  - they can be the same or different types

***Example***:
```// Import the HashMap class
import java.util.HashMap;

public class Main {
  public static void main(String[] args) {
    // Create a HashMap object called capitalCities
    HashMap<String, String> capitalCities = new HashMap<String, String>();

    // Add keys and values (Country, City)
    capitalCities.put("England", "London");
    capitalCities.put("Germany", "Berlin");
    capitalCities.put("Norway", "Oslo");
    capitalCities.put("USA", "Washington DC");
    System.out.println(capitalCities);
  }
}
```

***Output***:
```{USA=Washington DC, Norway=Oslo, England=London, Germany=Berlin}```  
  

## methods

.get(): ```capitalCities.get("England");```
***Output***: London

.remove(): ```capitalCities.remove("England");```

.clear(): ```capitalCities.clear();```

.size: ```capitalCities.size();```

.put()


## loops

    for (String i : capitalCities.keySet()) {
        System.out.println(i);
    }


Use the keySet() method if you only want the keys, and use the values() method if you only want the values


