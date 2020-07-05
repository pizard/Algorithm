# Use : permutations = []; permutation(dist[:i], [], permutations)
def permutation(candidates, PrePermutation, res):
    if len(candidates) == 0:
        res.append(PrePermutation)
        return;
    else:
        for i in range(len(candidates)):
            permutation(candidates[:i]+candidates[i+1:], PrePermutation + [candidates[i]], res)