/*-----------------------------------------------------------------------------------------*
   EXECUTION CODE MACRO 

   _laz prefix stands for LLM - Azure Zero-Shot
*------------------------------------------------------------------------------------------*/

%macro _laz_execution_code;

/*-----------------------------------------------------------------------------------------*
   Create payload
*------------------------------------------------------------------------------------------*/



/*-----------------------------------------------------------------------------------------*
   Create payload
*------------------------------------------------------------------------------------------*/

   filename inpay temp;
   
   data _null_;
      file inpay;
      input;
      put _infile_;
      datalines;
{
      "prompt": ["
        "How many plays did Shakespeare write?""
      ],
      "max_tokens": 8000,
      "temperature": 0,
      "frequency_penalty": 2,
      "n": 1
    }

;
run;

filename headd temp;

data _null_;
file headd;
put "api-key: f280112d275040608311f2920c9f1a28";
put "Accept: application/json";
run;


/* reference that file as IN= parm in PROC HTTP POST */
filename resp temp;
filename headero temp;
proc http 
 method="post"
 url="https://{{service}}.openai.azure.com/openai/deployments/{{deployment}}/completions?api-version=2024-10-21"
 ct="application/json"
 headerin= headd
 headerout= headero
 in=inpay
 out=resp; 
run;

data _NULL_;
    length message $32767.;
    infile headero scanover truncover;
    input @1 message $32767.;
    put message=;
run;

data _NULL_;
    length message $32767.;
    infile resp scanover truncover;
    input @1 message $32767.;
    put message=;
run;


/* POST https://{endpoint}/openai/deployments/{deployment-id}/completions?api-version=2024-10-21 */

libname respj json  fileref=resp;

%mend _laz_execution_code;
