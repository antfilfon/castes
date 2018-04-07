lower_caste_keywords = ['dalit', 'untouchable', 'sc_st', 'obc', 'lower_caste', 'minorities', 'backward_class']
upper_caste_keywords = ['upper_caste', 'brahmin', 'kshatriya', 'vaishya']
priviledge_keywords = ['government', 'democracy', 'election', 'college', 'education', 'scholar', 'merit', 'meritorious', 'employer', 'national', 'international', 'rich']
negative_aspect = ['poor', 'violence', 'disease', 'unhealthy', 'incident', 'crime']
positive_aspect = ['empathy', 'care', 'companion', 'friend', 'healthy', 'prosperity']
neutral_keywords = ['individual', 'man', 'woman', 'person', 'people', 'subject', 'object', 'human']

def add_to_graph(word, assoclist, graph):
    graph.add_node(word)
    for wtuple in assoclist:
        kword, kweight = wtuple
        graph.add_node(kword)
        graph.add_edge(word, kword, weight=kweight)

def recurse_add_(word, wvmodel, graph, depth=1, topn=5):
    if depth==1:
        # call add_to_graph and return
        alist = wvmodel.most_similar(word, topn=topn)
        add_to_graph(word, alist, graph)
        return
    else:
        # generate wordlist, then call recurse_add_ with each word in wordlist, with depth-1
        alist = wvmodel.most_similar(word, topn=topn)
        for wtuple in alist:
            aword, _ = wtuple
            recurse_add_(aword, wvmodel, graph, depth=depth-1, topn=topn)

def word_add_(word, wvmodel, lista, depth=1, topn=5):
    if depth==1:
        lista[word] = wvmodel.most_similar(word, topn=topn)
        return
    else:
        for wtuple in wvmodel.most_similar(word, topn=topn):
            aword, _ = wtuple
            word_add_(aword, wvmodel, lista, depth=depth-1, topn=topn)