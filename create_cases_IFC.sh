#!/bin/bash
#!/bin/bash
python FOL_IFC.py case1.txt > case_1_out_IFC.txt
mv case_1_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case2.txt > case_2_out_IFC.txt
mv case_2_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case3.txt > case_3_out_IFC.txt
mv case_3_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case4.txt > case_4_out_IFC.txt
mv case_4_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case5.txt > case_5_out_IFC.txt
mv case_5_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case6.txt > case_6_out_IFC.txt
mv case_6_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case7.txt > case_7_out_IFC.txt
mv case_7_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case8.txt > case_8_out_IFC.txt
mv case_8_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case9.txt > case_9_out_IFC.txt
mv case_9_out_IFC.txt ./IFC_test_transcripts
python FOL_IFC.py case10.txt > case_10_out_IFC.txt
mv case_10_out_IFC.txt ./IFC_test_transcripts

