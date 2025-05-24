import time
import json
import statistics
import requests
from typing import List, Dict

def benchmark_rest(tests: List[Dict]) -> Dict:
    latencies = []
    results = []
    
    for test in tests:
        start_time = time.time()
        response = requests.request(
            method=test["method"],
            url=test["url"],
            headers=test.get("headers", {}),
            json=test.get("body")
        )
        latency = (time.time() - start_time) * 1000  # Convert to ms
        
        results.append({
            "url": test["url"],
            "method": test["method"],
            "status_code": response.status_code,
            "latency_ms": latency
        })
        latencies.append(latency)
    
    return {
        "tests": results,
        "average_latency_ms": statistics.mean(latencies),
        "min_latency_ms": min(latencies),
        "max_latency_ms": max(latencies)
    }

def benchmark_graphql(tests: List[Dict]) -> Dict:
    latencies = []
    results = []
    
    for test in tests:
        start_time = time.time()
        response = requests.post(
            test["url"],
            json={"query": test["query"]},
            headers=test.get("headers", {"Content-Type": "application/json"})
        )
        latency = (time.time() - start_time) * 1000  # Convert to ms
        
        results.append({
            "url": test["url"],
            "query": test["query"],
            "status_code": response.status_code,
            "latency_ms": latency
        })
        latencies.append(latency)
    
    return {
        "tests": results,
        "average_latency_ms": statistics.mean(latencies),
        "min_latency_ms": min(latencies),
        "max_latency_ms": max(latencies)
    }

def main():
    # Load test configurations
    with open("benchmarks/rest_tests.json") as f:
        rest_tests = json.load(f)
    with open("benchmarks/graphql_tests.json") as f:
        graphql_tests = json.load(f)

    print("🚀 Running API benchmarks...")
    
    # Run benchmarks
    rest_result = benchmark_rest(rest_tests)
    graphql_result = benchmark_graphql(graphql_tests)

    # Print results
    print("\n📊 Results:")
    print(f"REST Average Latency: {rest_result['average_latency_ms']:.2f}ms")
    print(f"GraphQL Average Latency: {graphql_result['average_latency_ms']:.2f}ms")

    winner = (
        "REST" if rest_result["average_latency_ms"] < graphql_result["average_latency_ms"]
        else "GraphQL"
    )
    print(f"\n🏆 Winner: {winner} is faster!")

    # Save detailed results
    results = {
        "rest": rest_result,
        "graphql": graphql_result,
        "winner": winner
    }
    
    with open("results/output.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main() 