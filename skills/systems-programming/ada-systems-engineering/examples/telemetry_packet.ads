package Telemetry_Packet is
   pragma Pure;
   type Millivolts is range 0 .. 5_000 with Size => 16;
   type Channel_Index is range 1 .. 4;
   type Voltage_Array is array (Channel_Index) of Millivolts;

   type Sensor_Frame is record
      Header_Magic : Millivolts := 4_095;
      Channels     : Voltage_Array := (others => 0);
   end record;

   function Mean_Voltage (F : Sensor_Frame) return Millivolts
     with Post => Mean_Voltage'Result <= 5_000;
end Telemetry_Packet;
