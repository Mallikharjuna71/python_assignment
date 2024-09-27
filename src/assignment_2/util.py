
""" Given the participants' score sheet for your University Sports Day, you are required
to find the runner-up score."""

def runner_up_score(scores):
    first=scores[0]
    runnerUp=0

    for i in scores:
        if i > first:
            runnerUp=first
            first=i

    return runnerUp

# def runner_up_score():
#     arr = map(int, input().split())
#     arr = sorted(list(set(arr)), reverse=True)
#     r = arr[1]
#     return r