from src.data_loader import AnimeDataLoader
from src.vectore_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger=get_logger(__name__)

def main():
    try:
        logger.info("Starting the pipeline")
        loader=AnimeDataLoader(original_csv="data/anime_with_synopsis.csv", processed_csv="data/updated_anime.csv")
        processed_csv = loader.load_and_process()
        
        logger.info("Data loaded and processed successfully")
        
        vector_builder=VectorStoreBuilder(csv_path=processed_csv, persist_dir="chroma_db")
        vector_builder.build_and_save_vectorstore()
        
        logger.info("Vector store built and saved successfully")
        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Failed to execute the pipeline. Error: {str(e)}")
        raise CustomException("Erorr occurred while executing the pipeline.")
    
if __name__=="__main__":
    main()
