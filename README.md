# 一路黔行 · RideAlong

**简体中文** | [English](README.en.md)

一路黔行是一个以贵州旅游与地域文化为主题的 Web 课程团队项目，结合城市介绍、文化内容、地图路线查询和用户故事分享，为用户提供探索贵州的网页入口。

项目采用 Django 服务端模板渲染，使用 SQLite 保存数据，通过 Leaflet、Folium 与外部地图服务展示地图和驾车路线。

## 作品演示

[点击观看项目演示视频（哔哩哔哩）](https://www.bilibili.com/video/BV1i1421y7fA/)

## 功能概览

- **旅游内容浏览**：首页、城市介绍、文化介绍及五个文化专题页面。
- **路线查询**：选择出发地和目的地的城市、区县，根据数据库中的经纬度请求 OSRM 驾车路线，在地图上绘制路径和起终点标记。
- **交互地图**：地图浏览、点击选点，以及基于 Esri 服务的逆地理编码。
- **故事分享**：故事列表和详情、Markdown 内容展示，以及发布、编辑、删除和图片上传相关逻辑。
- **用户系统**：注册、登录、退出、个人资料与头像更新、个人故事列表；较大的头像会缩放至 300 × 300 范围内。
- **管理入口**：Django Admin 管理后台。

“我的行程”目前为页面入口，不能视为已经实现完整的行程保存与管理功能。

## 技术栈

| 层次 | 技术 |
| --- | --- |
| 后端 | Python、Django、Django ORM |
| 数据存储 | SQLite |
| 页面与交互 | Django Templates、HTML、CSS、JavaScript、jQuery、HTMX |
| 表单与内容 | django-crispy-forms、crispy-bootstrap5、django-mdeditor、Markdown |
| 地图与路线 | Leaflet、Folium、OpenStreetMap 瓦片、Esri 地理编码、OSRM |
| 图片处理 | Pillow |

## 项目结构

```text
ridealong/                 # 本 README 所在目录
├── manage.py              # Django 命令入口
├── requirements.txt       # 原始依赖清单，存在兼容与完整性问题
├── db.sqlite3             # 随项目提供的数据库
├── ridealong/             # settings、URL、WSGI、ASGI 配置
├── pages/                 # 首页、城市、文化与路线选择页面
├── city/                  # 城市、区县模型和数据加载命令
├── route/                 # 地图展示与 OSRM 路线请求
├── story/                 # 故事模型、视图与模板
├── users/                 # 用户资料、表单、信号与模板
├── static/                # 公共图片、样式等静态资源
└── media/                 # 头像、故事图片等媒体资源
```

## 本地运行：Conda

以下为根据源码整理的复现步骤，尚未完成干净环境下的依赖安装与全流程验证。使用 Python 3.10 复现历史依赖；不要直接使用 Python 3.13 安装这些旧版本。

### 1. 创建环境

在 Anaconda Prompt 或已经初始化 Conda 的终端中执行：

```shell
conda create -n ridealong python=3.10 pip -y
conda activate ridealong
python --version
```

### 2. 进入源码目录

进入包含 `manage.py` 的目录。如果仓库根目录就是本目录，可直接在此打开终端；如果外层还有 `ridealong` 文件夹，先执行：

```shell
cd ridealong
```

### 3. 安装依赖

```shell
python -m pip install "Django==4.0.2" "django-crispy-forms==2.0" "crispy-bootstrap5==0.7" "Pillow==9.0.1" django-mdeditor Markdown folium polyline requests
```

### 4. 检查配置和数据库

```shell
python manage.py check
python manage.py showmigrations
```

优先保留随项目提供的 `db.sqlite3` 和 `media/`，避免丢失展示数据及图片。若有未应用的迁移，先复制数据库备份，再执行：

```shell
python manage.py migrate
```

仅在新建数据库、需要初始化城市与区县数据时使用：

```shell
python manage.py load_data
```

**注意：`load_data` 会先删除现有城市和区县数据，并可能通过模型关系影响关联数据。不要对已有展示数据库直接重复执行。** 此命令不负责恢复故事、用户或媒体文件。

### 5. 启动服务

```shell
python manage.py runserver
```

打开 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)，保持终端运行，按 `Ctrl+C` 停止。

下次启动只需激活环境、进入源码目录并执行 `python manage.py runserver`。当前部分地图模板写死了 `http://localhost:8000`，更换端口时还需同步调整这些链接。

### 6. 可选：创建管理员

```shell
python manage.py createsuperuser
```

随后访问 `/admin/`。普通用户可以通过 `/register/` 注册。

## 页面入口

| 路径 | 页面 |
| --- | --- |
| `/` | 首页 |
| `/city/` | 城市介绍 |
| `/culture/` | 文化介绍 |
| `/route/` | 出发地与目的地选择 |
| `/route/showmap` | 交互选点地图 |
| `/story/list/` | 故事列表 |
| `/story/add/` | 发布故事，需要登录 |
| `/register/`、`/login/` | 注册、登录 |
| `/profile/` | 个人资料，需要登录 |
| `/about/` | 关于页面 |
| `/admin/` | 管理后台 |

## 团队贡献与素材

这是课程团队项目。源码本身不足以确认每位成员的负责范围，本文不将团队成果归为某一位成员。

本文未声明开源许可证；使用和再分发需确认相应授权，并保留地图及其他第三方资源要求的署名。
