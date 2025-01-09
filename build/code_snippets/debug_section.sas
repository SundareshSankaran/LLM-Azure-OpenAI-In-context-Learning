/*-----------------------------------------------------------------------------------------*
   DEBUG Macro
   Inputs:
      1. var_path: a path to a list of variables, tab separated with a variable and value column.

   Outputs:
      1. Macro variables populated with values
*------------------------------------------------------------------------------------------*/

%macro _laz_debug(var_path);

/*-----------------------------------------------------------------------------------------*
   Capture list of parameters and save them as macro variables
*------------------------------------------------------------------------------------------*/

/* proc import datafile=&var_path. 
   DBMS=DLM
   out=WORK.INPUTVARS
   replace;
   delimiter="09"x;
run;

data _null_;
    set WORK.INPUTVARS;
    call symput(variable,value);
run;

%put NOTE: A list of current macro variables follow. ;
%put _all_; */

%mend _laz_debug;