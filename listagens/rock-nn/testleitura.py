from tester import apply_model

def main():
    full_path = "/home/joao/projects/python/notebooks"
    apply_model(
        model_file=f"{full_path}/images/Berea500/pixeldataBerea500-nn-model.pt", 
        image=f"{full_path}/images/Berea200/I22.png", 
        output=f"{full_path}/images/Berea200/test",
        save=True)

if __name__ == "__main__":
    main()