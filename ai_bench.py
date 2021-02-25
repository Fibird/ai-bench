from ai_benchmark import AIBenchmark
import os

def main():
    env_dist = os.environ

    runComplete = env_dist.get('RUN_COMPLETE', 'true')
    onlyInference = env_dist.get('ONLY_INFERENCE', 'false')
    onlyTraining = env_dist.get('ONLY_TRAINING', 'false')

    if runComplete == 'false':
        if onlyInference == 'true':
            result = benchmark.run_inference()
        elif onlyTraining == 'true':
            result = benchmark.run_training()
    else:
        results = AIBenchmark().run()
    
    print(result)

if __name__ = '__main__':
    main()
