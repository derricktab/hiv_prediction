This model is trained to predict the resistance of HIV-1 to Fosamprenavir (FPV), a protease inhibitor used in the treatment of HIV/AIDS. Utilizing genetic sequence data from the HIV-1 virus, the model employs deep learning techniques to analyze mutations within the protease enzyme that may confer resistance to Fosamprenavir. By processing numerical representations of these sequences through convolutional neural networks, the model can effectively distinguish between resistant and non-resistant strains. This capability supports healthcare providers in optimizing antiretroviral therapy by enabling personalized treatment plans based on the genetic profile of the virus found in individual patients.




The model takes as input a string representing the amino acid sequence of the HIV-1 protease enzyme. Each character in the string corresponds to a specific amino acid, represented by its standard single-letter code.

SAMPLE API INPUT
{
  "sequence": "PQITLWQRPLVTIKIGGQLKEALLDTGADDTVLEEMNLPGRWKPKMIGGIGGFIKVRQYDQILIEICGHKAIGTVLVGPTPVNIIGRNLLTQIGCTLNF"
}


SAMPLE RESPONSE FROM API
{
  "resistance": 1
}


In the model response, 1 represents that the model predicts the HIV-1 sequence data provided as resistant to FPV, whereas a 0 indicates susceptibility (non-resistance) to the drug.

