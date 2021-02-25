from ai_benchmark import AIBenchmark
import os

def main():
    env_dist = os.environ

    runComplete = env_dist.get('RUN_COMPLETE', 'true')
    onlyInference = env_dist.get('ONLY_INFERENCE', 'false')
    onlyTraining = env_dist.get('ONLY_TRAINING', 'false')

    if runComplete == 'false':
        if onlyInference == 'true':
            result = AIBenchmark(use_CPU=true, verbose_level=1).run_inference()
            print(result)
        elif onlyTraining == 'true':
            result = AIBenchmark(use_CPU=true, verbose_level=1).run_training()
            print(result)
    else:
        results = AIBenchmark(use_CPU=true, verbose_level=1).run()
        print(result)
    

if __name__ == '__main__':
    main()
