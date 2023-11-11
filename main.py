import click
from loguru import logger
from pipelines import features_extraction , model , predict

@click.group(chain=True , invoke_without_command=True)
@click.option('--model_name', type=str, default='all-mpnet-base-v2',help='name of the transformer',required=True)
@click.option('--cache_folder', type=str , envvar='TRANSFORMERS_CACHE',help='name of the transformer',required=True)
@click.pass_context
def command_line(ctx:click.core.Context):
    """This function chain all pipelines

    """
    subcommand = ctx.invoked_subcommand
    if subcommand is None:
        logger.info('No command provided')
    ctx.obj['model_name'] = model_name
    # ctx.obj['cache_folder'] = cache_folder

command_line.add_command(features_extraction)
command_line.add_command(model)
command_line.add_command(predict)


if __name__ == "__main__":
    command_line(
        obj=()
    )