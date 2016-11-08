from publicsuffix import PublicSuffixList,fetch
psl_file = fetch()
psl = PublicSuffixList(psl_file)
print psl.get_public_suffix("http://www.example.com/dsadsadsadsa")