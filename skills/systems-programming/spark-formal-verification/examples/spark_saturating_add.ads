package Spark_Saturating_Add with SPARK_Mode => On is
   subtype U16 is Natural range 0 .. 65_535;

   function Saturating_Add (A, B : U16) return U16 with
     Global => null,
     Depends => (Saturating_Add'Result => (A, B)),
     Contract_Cases =>
       (A + B <= 65_535 => Saturating_Add'Result = A + B,
        A + B >  65_535 => Saturating_Add'Result = 65_535);
end Spark_Saturating_Add;
