
docker build -t data_descriptors_and_metaclasses -f config/data_descriptors_and_metaclasses.Dockerfile .
docker run --privileged -ti -v ${PWD}:/usr/local/bin/data_descriptors_and_metaclasses -p 8888:8888 data_descriptors_and_metaclasses