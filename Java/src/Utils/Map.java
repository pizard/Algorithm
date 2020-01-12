package Utils;

import java.util.*;

public class Map {
    // num  0: ascending, 1: descending
    public static <K, V extends Comparable<? super V>> java.util.Map<K, V> sortByValue(java.util.Map<K, V> map, int num) {
        List<java.util.Map.Entry<K, V>> list = new ArrayList<>(map.entrySet());
        if(num == 0)
            list.sort(java.util.Map.Entry.comparingByValue());
        else
            list.sort(java.util.Map.Entry.comparingByValue(Comparator.reverseOrder()));

        java.util.Map<K, V> result = new LinkedHashMap<>();
        for (java.util.Map.Entry<K, V> entry : list) {
            result.put(entry.getKey(), entry.getValue());
        }

        return result;
    }
}
