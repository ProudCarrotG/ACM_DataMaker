import os.path
import subprocess

import utils.logging_init
import utils.walk_path

logger = utils.logging_init.logging_init(__name__)

if __name__ == '__main__':

    logger.info("开始扫描std目录下的文件")
    stdPath = utils.walk_path.walk_path('.\\std')
    logger.info("开始扫描make目录下的文件")
    makePath = utils.walk_path.walk_path('.\\make')

    for stdpath in stdPath:
        stdname = os.path.basename(stdpath)
        if stdname.split('.')[1] != 'exe':
            continue

        logger.info(f"已获取{stdname}的正解二进制文件")
        logger.info(f"正在查找对应的数据制造文件")
        makepath = ''
        if stdname not in map(os.path.basename, makePath):
            logger.info(f"{stdname}没有对应的数据制造文件")
            continue
        else:
            for file in makePath:
                if stdname == os.path.basename(file):
                    makepath = file
                    break
        logger.info(f"已获取{stdname}的数据制造二进制文件")

        n = int(input('需要制作多少组数据？'))

        datapath = '.\\data\\' + stdname.split('.')[0]
        # os.mkdir(datapath)

        for i in range(n):
            logger.info(f'正在尝试制作{stdname}的第{i}个in文件')
            logger.debug(f'{makepath} > {datapath}\\{i}.in')

            subprocess.run(f'{makepath} > {datapath}\\{i}.in', shell=True)
            logger.info(f'.in文件制作命令执行结束')

            logger.info(f'正在尝试制作{stdname}的第{i}个out文件')
            logger.debug(f'{stdpath} < {datapath}\\{i}.in > {datapath}\\{i}.out')

            subprocess.run(f'{stdpath} < {datapath}\\{i}.in > {datapath}\\{i}.out', shell=True)
            logger.info(f'.out文件制作命令执行结束')

        logger.info(f'{stdname}执行完毕')
