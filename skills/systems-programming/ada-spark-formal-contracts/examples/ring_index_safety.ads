pragma SPARK_Mode (On);
package Ring_Index_Safety is
   subtype Ring_Capacity is Positive range 1 .. 4096;
   subtype Ring_Offset   is Natural  range 0 .. 4095;

   function Next_Slot (Pos : Ring_Offset; Cap : Ring_Capacity) return Ring_Offset
     with Pre  => Pos < Cap,
          Post => Next_Slot'Result < Cap;
end Ring_Index_Safety;
