"""AWS Service Integration"""
import boto3
import os
from typing import Optional, Dict, Any


class AWSService:
    """AWS Service wrapper for S3, RDS, EC2, etc."""
    
    def __init__(self):
        self.aws_region = os.getenv('AWS_REGION', 'us-east-1')
        self.s3_client = boto3.client('s3', region_name=self.aws_region)
        self.rds_client = boto3.client('rds', region_name=self.aws_region)
        self.ec2_client = boto3.client('ec2', region_name=self.aws_region)
    
    def upload_to_s3(self, file_path: str, bucket: str, object_name: Optional[str] = None) -> bool:
        """Upload file to S3 bucket"""
        try:
            if object_name is None:
                object_name = os.path.basename(file_path)
            
            self.s3_client.upload_file(file_path, bucket, object_name)
            return True
        except Exception as e:
            print(f"S3 upload error: {e}")
            return False
    
    def get_s3_object(self, bucket: str, object_name: str) -> Optional[bytes]:
        """Download object from S3"""
        try:
            response = self.s3_client.get_object(Bucket=bucket, Key=object_name)
            return response['Body'].read()
        except Exception as e:
            print(f"S3 download error: {e}")
            return None
    
    def list_rds_instances(self) -> list:
        """List all RDS database instances"""
        try:
            response = self.rds_client.describe_db_instances()
            return response.get('DBInstances', [])
        except Exception as e:
            print(f"RDS list error: {e}")
            return []
    
    def describe_ec2_instances(self) -> list:
        """Describe EC2 instances"""
        try:
            response = self.ec2_client.describe_instances()
            instances = []
            for reservation in response.get('Reservations', []):
                instances.extend(reservation.get('Instances', []))
            return instances
        except Exception as e:
            print(f"EC2 describe error: {e}")
            return []


# Global AWS service instance
aws_service = AWSService()
