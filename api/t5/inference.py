import json
import requests

## secrets.json format:
#
#   {
#       key: <API_KEY>
#   }
#

with open("secrets.json", "r") as read_file:
    data = json.load(read_file)

API_URL = "https://api-inference.huggingface.co/models/Falconsai/medical_summarization"
headers = {"Authorization": f"Bearer {data['key']}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Gender differences in brain development and in the prevalence of neuropsychiatric disorders such as depression have been reported. Gender differences in human brain might be related to patterns of gene expression. Microarray technology is one useful method for investigation of gene expression in brain. We investigated gene expression, cell types, and regional expression patterns of differentially expressed sex chromosome genes in brain. We profiled gene expression in male and female dorsolateral prefrontal cortex, anterior cingulate cortex, and cerebellum using the Affymetrix oligonucleotide microarray platform. Differentially expressed genes between males and females on the Y chromosome (DBY, SMCY, UTY, RPS4Y, and USP9Y) and X chromosome (XIST) were confirmed using real-time PCR measurements. In situ hybridization confirmed the differential expression of gender-specific genes and neuronal expression of XIST, RPS4Y, SMCY, and UTY in three brain regions examined. The XIST gene, which silences gene expression on regions of the X chromosome, is expressed in a subset of neurons. Since a subset of neurons express gender-specific genes, neural subpopulations may exhibit a subtle sexual dimorphism at the level of differences in gene regulation and function. The distinctive pattern of neuronal expression of XIST, RPS4Y, SMCY, and UTY and other sex chromosome genes in neuronal subpopulations may possibly contribute to gender differences in prevalence noted for some neuropsychiatric disorders. Studies of the protein expression of these sex-chromosome-linked genes in brain tissue are required to address the functional consequences of the observed gene expression differences.",
})

print(output)