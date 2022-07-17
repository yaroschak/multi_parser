DOCKER_COMPOSE_FILE=docker-compose_parser.yml

IS_RUNNING=`docker-compose -f $DOCKER_COMPOSE_FILE ps --services --filter "status=running"`


if [[ "$IS_RUNNING" != "" ]];
  then
    echo "The service is running!!!"
    docker-compose -f $DOCKER_COMPOSE_FILE down
  else
    echo "The service is not running!!!"
    docker-compose -f $DOCKER_COMPOSE_FILE up -d
fi


