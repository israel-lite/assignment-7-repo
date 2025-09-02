candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata like party, region, etc."""
    for name in args:
        if name not in candidates:
            # Initialize with vote count and any extra metadata
            candidates[name] = {"votes": 0}
            candidates[name].update(kwargs)
        else:
            print(f"{name} already registered.")

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before."""
    if voter_id in voters:
        return f"Voter {voter_id} has already voted."
    if candidate not in candidates:
        return f"Candidate {candidate} not found."
    
    candidates[candidate]["votes"] += 1
    voters.add(voter_id)
    return f"Vote casted for {candidate}."

def election_result():
    """Return the winner(s)."""
    if not candidates:
        return {"winners": [], "candidates": candidates}
    
    # Find max votes
    max_votes = max(c["votes"] for c in candidates.values())
    
    # Get all candidates with max votes (to handle ties)
    winners = [name for name, data in candidates.items() if data["votes"] == max_votes]
    
    return {"winners": winners, "candidates": candidates}


# Example usage:
register_candidates("Alice", "Bob", party="Independent", region="North")
print(cast_vote("V1", "Alice"))
print(cast_vote("V2", "Bob"))
print(cast_vote("V1", "Bob"))  # Duplicate voter
print(election_result())

