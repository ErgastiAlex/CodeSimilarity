#!/opt/homebrew/lib/python3.9
import sys
import os

def get_similar_codes(dir):
    files = os.listdir(dir)
    files = [os.path.join(dir, f) for f in files]
    files = [f for f in files if os.path.isfile(f)]
    files = [f for f in files if f.endswith('.py')]

    for f1 in files:
        try:
            if f1.endswith('.py'):
                other_files = [f for f in files if f != f1]
                similarity = {}
                for f2 in other_files:
                    try:
                        cmd = f'pycode_similar {f1} {f2}'
                        output = os.popen(cmd).readlines()
                        percentage = float(output[2].split("%")[0])
                        similarity[f2] = percentage
                    except:
                        continue
                sorted_similarity = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
                # Remove codes that have similarity == 100.0
                sorted_similarity = [x for x in sorted_similarity if x[1] != 100.0]
                # Copy the top 10 similar codes to a new directory
                new_dir = os.path.join(dir, 'similar_codes')
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                for i in range(10):
                    f2 = sorted_similarity[i][0]
                    print(f1, f2, sorted_similarity[i][1])
                    cmd = f'cp {f2} {new_dir}'
                    os.system(cmd)
                cmd = f'cp {f1} {new_dir}'
                os.system(cmd)
                break
        except Exception as e:
            pass

if __name__ == '__main__':
    get_similar_codes(sys.argv[1])